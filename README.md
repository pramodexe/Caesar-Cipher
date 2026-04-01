CAESAR(1)                    User Commands                   CAESAR(1)
======================================================================

NAME
    caesar - command-line Caesar cipher encryption/decryption tool

SYNOPSIS
    python caesar.py -e -t "TEXT" -s SHIFT
    python caesar.py -d -t "TEXT" -s SHIFT
    python caesar.py -b -t "TEXT"
    python caesar.py -h

DESCRIPTION
    The caesar tool performs classical Caesar-cipher rotation on
    alphabetical text. It supports encryption, decryption, and full
    bruteforce rotation attempts (0–25). Non-alphabetic characters are
    preserved unchanged.

OPTIONS
    -e, --encrypt
           Encrypt the provided text using the shift value.

    -d, --decrypt
           Decrypt the provided text using the shift value.

    -b, --bruteforce
           Attempt all possible 26 rotations and print results.

    -s SHIFT, --shift SHIFT
           Rotation amount (0–25). Required for -e and -d modes.

    -t TEXT, --text TEXT
           Input text to be processed.

    -h, --help
           Display the help menu and exit.

EXAMPLES
    Bruteforce decrypt an unknown message:
           python caesar.py -b -t "khoor zruog"

    Encrypt a message:
           python caesar.py -e -t "hello" -s 3

    Decrypt a message:
           python caesar.py -d -t "khoor" -s 3

ERROR HANDLING
    The tool uses exception catching to prevent crashes. Common error
    cases include:
           • Missing -t text argument
           • Using -e or -d without the -s shift value
           • Providing non-integer shift values

EXIT STATUS
    0     Successful execution
    1     Invalid arguments or runtime error

AUTHOR
    Written as a standalone educational implementation of the
    classical Caesar cipher.

SEE ALSO
    python(1)  
    argparse documentation: https://docs.python.org/3/library/argparse.html

======================================================================
CAESAR(1)                    User Commands                   CAESAR(1)
