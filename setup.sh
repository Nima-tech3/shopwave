#!/usr/bin/env sh

_confirm(){
  # USAGE: `confirm [quastion_to_confirm] [context_for_the_quastion]`
  while :; do
    printf "%s\n%s\n\nProceed? (n/Y)\n> " "$1" "$2"
    IFS= read -r _confirmAnswer
    if [ -z "$_confirmAnswer" ]; then
      _confirmAnswer=y
    fi
    case "$_confirmAnswer" in
      y|Y)
        printf "%s\n---\n" "Confirmed."
        return 0
        ;;
      n|N)
        printf "%s\n---\n" "Refusal accepted."
        return 1
        ;;
      *)
        printf "%s\n---\n" "Invalid answer."
        continue
        ;;
    esac
  done
}
_exit(){
  printf "$1\n"
  exit 1
}

_confirm "current directory: $(pwd)" "Changing to Project directory."
if [ "$?" -eq 0 ]; then
  cd "$(dirname "$0")" || _exit "cd failed."
else
  exit 1
fi

_confirm "" "First time Initialisation setup seqence."
if [ "$?" -eq 1 ]; then
  _confirm "" "Running project."
  . venv/bin/activate || _exit "Initilisation failed."
  python3 manage.py runserver || _exit "Running failed."
fi

if ! command -v python3 >/dev/null 2>&1; then
   printf "Python3 was not found\n"; exit 1;
fi
_confirm "" "Initialising new Python VENV."
if [ "$?" -eq 0 ]; then
  python3 -m venv venv || _exit "Initilisation failed."
  . venv/bin/activate || _exit "Initilisation failed."
else
  exit 1
fi

_confirm "$(cat requirements.txt)" "Installing required packages."
if [ "$?" -eq 0 ]; then
  python3 -m pip install -r requirements.txt || _exit "Inistallation failed."
else
  exit 1
fi

_confirm "" "Initialising Project spesific envirment."
if [ "$?" -eq 0 ]; then
  python3 manage.py migrate || _exit "Initialisation failed."
else
  exit 1
fi
_confirm "" "Running project."
if [ "$?" -eq 0 ]; then
  python3 manage.py runserver || _exit  "Running failed."
else
  exit 1
fi

# AI:R
