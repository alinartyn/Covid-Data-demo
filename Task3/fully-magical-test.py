import sys

MAGICAL_WORDS = ['alohamora', 'expecto patronum']

# Assume 100% magic
fully_magical = True

# Attmept to disprove assumption: if user did not input any words
if len(sys.argv) < 2:
    fully_magical = False

# Attempt to disprove assumption: check if any of the words are non magical
for item in sys.argv[1:]:
    if item not in MAGICAL_WORDS:
        fully_magical = False


if fully_magical:
    print("100% magic! ✨")
else:
    print("Nothing to see here, move along ... 🤫")