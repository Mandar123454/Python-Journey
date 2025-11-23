import os, re, runpy, traceback, sys, builtins, time
from pathlib import Path

"""Verification harness.
Now attempts to execute more scripts by:
1. Injecting a dummy input() that returns a safe default.
2. Allowing simple scripts with smtplib / tkinter markers to be skipped (GUI/email).
3. Reporting previously skipped interactive scripts separately.

GUI (tkinter) scripts remain skipped to avoid windows popping up.
Email script skipped unless EMAIL_SENDER is set.
"""

ROOT = Path(__file__).parent
PATTERN = re.compile(r'^\d')

GUI_MARKERS = ['tkinter', 'mainloop(', 'Canvas', 'Button(', 'messagebox']
EMAIL_MARKERS = ['smtplib', 'EmailMessage']
INPUT_MARKER = 'input('
LONG_RUNNING_MARKERS = ['while True', 'play again? (yes/no):']

results = []

original_input = builtins.input
def dummy_input(prompt=''):
    # Return a value that works for most casts to int/str/bool
    return '1'

for file in sorted(ROOT.iterdir(), key=lambda p: p.name):
    if file.is_file() and file.suffix == '.py' and PATTERN.match(file.name):
        code = file.read_text(encoding='utf-8', errors='ignore')
        markers_found = []
        if any(m in code for m in GUI_MARKERS):
            results.append((file.name, 'SKIP_GUI', 'tkinter/GUI'))
            continue
        if any(m in code for m in EMAIL_MARKERS) and not os.getenv('EMAIL_SENDER'):
            results.append((file.name, 'SKIP_EMAIL', 'email creds not set'))
            continue
        # Detect long-running / interactive loop style games
        if any(m in code for m in LONG_RUNNING_MARKERS):
            results.append((file.name, 'SKIP_LONG', 'long-running interactive loop'))
            continue
        uses_input = INPUT_MARKER in code
        if uses_input:
            builtins.input = dummy_input
        try:
            runpy.run_path(str(file), run_name='__main__')
            results.append((file.name, 'OK', ''))
        except SystemExit as e:
            results.append((file.name, 'OK(SystemExit)', f'code={e.code}'))
        except Exception:
            results.append((file.name, 'ERROR', traceback.format_exc().splitlines()[-1]))
        finally:
            if uses_input:
                builtins.input = original_input

# Summary
ok = sum(1 for r in results if r[1].startswith('OK'))
err = sum(1 for r in results if r[1] == 'ERROR')
skip = sum(1 for r in results if r[1].startswith('SKIP'))
print(f'Total checked: {len(results)} | OK: {ok} | Errors: {err} | Skipped: {skip}')
for name, status, info in results:
    print(f'{name:<35} {status:<12} {info}')

if err:
    sys.exit(1)
