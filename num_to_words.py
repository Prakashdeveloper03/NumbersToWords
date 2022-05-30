# num2words is a library that converts numbers like 2001 to words like two thousand and one.
# It supports multiple languages
# And can even generate ordinal numbers like forty-second.
from num2words import num2words  # pip install num2words

# gets the user input as integer value and stores it in `num` variable
num = int(input("Enter the number : "))

print(
    f"{num} in normal format: {num2words(num)}"
)  # prints the number in 'normal' format
print(
    f"{num} in ordinal format: {num2words(num, to='ordinal')}"
)  # prints the number in 'ordinal' format
print(
    f"{num} in ordinal number format: {num2words(num, to='ordinal_num')}"
)  # prints the number in 'ordinal normal' format
print(
    f"{num} in year format: {num2words(num, to='year')}"
)  # prints the number in 'year' format
print(
    f"{num} in currency format: {num2words(num, to='currency')}"
)  # prints the number in 'currency' format

# languages supported by 'num2words' are stored as a dict object
languages = {
    "en": "English",
    "ar": "Arabic",
    "cz": "Czech",
    "de": "German",
    "dk": "Danish",
    "es": "Spanish",
    "fr": "French",
    "he": "Hebrew",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "kn": "Kannada",
    "ko": "Korean",
    "pt": "Portuguese",
    "ru": "Russian",
    "vi": "Vietnamese",
    "nl": "Dutch",
    "uk": "Ukrainian",
}
print("\nNumber word in different languages:\n")
for (
    language_code,
    language_name,
) in languages.items():  # iterates through the languages dict object
    # prints the number in all supported languages
    print(f"{num} in {language_name} language is {num2words(num, lang=language_code)}")
