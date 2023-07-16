import os
import sys

class TerminalColors:
    Green       = '\033[92m'
    Warning     = '\033[93m'
    Fail        = '\033[91m'

try:
    import pandas as pd
    print(f"{TerminalColors.Green}Module 'Pandas' found and imported!{TerminalColors.End}")
except ImportError:
    print(f"{TerminalColors.Fail}Module 'Pandas' not found, please install it with: python3 -m pip install -U pandas{TerminalColors.End}")
    print(f"{TerminalColors.Warning}{TerminalColors.Underline}Do you want to install it now? (yes/no){TerminalColors.End}")
    Choice = str(input())
    if Choice.lower() == 'y' or Choice.lower() == 'yes':
        try:
            os.system('python3 -m pip install -U pandas')
        except:
            os.system('pip install pandas')
        print(f"{TerminalColors.Green}Module 'Pandas' installed successfully!{TerminalColors.End}")
        try:
            import pandas as pd
            print(f"{TerminalColors.Green}Module 'Pandas' found and imported!{TerminalColors.End}")
        except ImportError:
            print(f"{TerminalColors.Fail}Module 'Pandas' not found, please reinstall it with: python3 -m pip install -U pandas{TerminalColors.End}")
            sys.exit()
    else:
        print(f"{TerminalColors.Fail}Installation 'Pandas' aborted!{TerminalColors.End}")

try:
    from dash import Dash, dcc, html
    print(f"{TerminalColors.Green}Module 'Dash' found and imported!{TerminalColors.End}")
except ImportError:
    print(f"{TerminalColors.Fail}Module 'Dash' not found, please install it with: python3 -m pip install -U dash{TerminalColors.End}")
    print(f"{TerminalColors.Warning}{TerminalColors.Underline}Do you want to install it now? (yes/no){TerminalColors.End}")
    Choice = str(input())
    if Choice.lower() == 'y' or Choice.lower() == 'yes':
        try:
            os.system('python3 -m pip install -U dash')
        except:
            os.system('pip install dash')
        print(f"{TerminalColors.Green}Module 'Dash' installed successfully!{TerminalColors.End}")
        try:
            from dash import Dash, dcc, html
            print(f"{TerminalColors.Green}Module 'Dash' found and imported!{TerminalColors.End}")
        except ImportError:
            print(f"{TerminalColors.Fail}Module 'Dash' not found, please reinstall it with: python3 -m pip install -U dash{TerminalColors.End}")
            sys.exit()
    else:
        print(f"{TerminalColors.Fail}Installation 'Dash' aborted!{TerminalColors.End}")