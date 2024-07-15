from string_utils import StringUtils
import pytest

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitilize_regular_string(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"

def test_capitilize_already_capitalized(string_utils):
    assert string_utils.capitilize("Skypro") == "Skypro"

def test_capitilize_empty_string(string_utils):
    assert string_utils.capitilize("") == ""

def test_capitilize_single_letter(string_utils):
    assert string_utils.capitilize("s") == "S"
    assert string_utils.capitilize("S") == "S"

def test_capitilize_multiple_words(string_utils):
    assert string_utils.capitilize("skypro education") == "Skypro education"


@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_trim_leading_spaces(string_utils):
    assert string_utils.trim("   skypro") == "skypro"

def test_trim_no_leading_spaces(string_utils):
    assert string_utils.trim("skypro") == "skypro"

def test_trim_only_spaces(string_utils):
    assert string_utils.trim("     ") == ""

def test_trim_empty_string(string_utils):
    assert string_utils.trim("") == ""

def test_trim_mixed_content(string_utils):
    assert string_utils.trim("   skypro   ") == "skypro   "

# Негативные тесты
def test_trim_non_string_input(string_utils):
    with pytest.raises(AttributeError):
        string_utils.trim(None)

    with pytest.raises(AttributeError):
        string_utils.trim(123)

    with pytest.raises(AttributeError):
        string_utils.trim(["   skypro"])

    with pytest.raises(AttributeError):
        string_utils.trim({"text": "   skypro"})

# Граничные значения
def test_trim_single_space(string_utils):
    assert string_utils.trim(" ") == ""

def test_trim_single_non_space_char(string_utils):
    assert string_utils.trim("a") == "a"

def test_trim_multiple_lines(string_utils):
    assert string_utils.trim("   \nskypro\n   ") == "\nskypro\n   "



@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_to_list_default_delimeter(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]

def test_to_list_custom_delimeter(string_utils):
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]

def test_to_list_empty_string(string_utils):
    assert string_utils.to_list("") == []

def test_to_list_no_delimeter_in_string(string_utils):
    assert string_utils.to_list("abc") == ["abc"]

def test_to_list_multiple_delimiters(string_utils):
    assert string_utils.to_list("a,,b,c,,d", ",") == ["a", "", "b", "c", "", "d"]

def test_to_list_with_spaces(string_utils):
    assert string_utils.to_list("a, b, c, d") == ["a", " b", " c", " d"]

def test_to_list_custom_delimeter_long(string_utils):
    assert string_utils.to_list("one;two;three", ";") == ["one", "two", "three"]

# Негативные тесты
def test_to_list_non_string_input(string_utils):
    with pytest.raises(AttributeError):
        string_utils.to_list(None)

    with pytest.raises(AttributeError):
        string_utils.to_list(123)

    with pytest.raises(AttributeError):
        string_utils.to_list(["a,b,c"])

    with pytest.raises(AttributeError):
        string_utils.to_list({"text": "a,b,c"})

def test_to_list_invalid_delimeter_type(string_utils):
    with pytest.raises(TypeError):
        string_utils.to_list("a,b,c", None)

    with pytest.raises(TypeError):
        string_utils.to_list("a,b,c", 123)

    with pytest.raises(TypeError):
        string_utils.to_list("a,b,c", [";"])

# Граничные случаи
def test_to_list_single_character(string_utils):
    assert string_utils.to_list("a") == ["a"]

def test_to_list_single_delimeter(string_utils):
    assert string_utils.to_list(",") == ["", ""]

def test_to_list_leading_trailing_delimiters(string_utils):
    assert string_utils.to_list(",a,b,c,") == ["", "a", "b", "c", ""]


@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_contains_symbol_present(string_utils):
    assert string_utils.contains("SkyPro", "S") == True

def test_contains_symbol_absent(string_utils):
    assert string_utils.contains("SkyPro", "U") == False

def test_contains_empty_string(string_utils):
    assert string_utils.contains("", "a") == False

def test_contains_symbol_at_end(string_utils):
    assert string_utils.contains("SkyPro", "o") == True

def test_contains_symbol_at_start(string_utils):
    assert string_utils.contains("SkyPro", "S") == True

def test_contains_multiple_occurrences(string_utils):
    assert string_utils.contains("SkyProSky", "S") == True

def test_contains_case_sensitive(string_utils):
    assert string_utils.contains("SkyPro", "s") == False

def test_contains_whitespace(string_utils):
    assert string_utils.contains("Sky Pro", " ") == True

# Негативные тесты
def test_contains_non_string_input_string(string_utils):
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")

    with pytest.raises(AttributeError):
        string_utils.contains(123, "1")

    with pytest.raises(AttributeError):
        string_utils.contains(["SkyPro"], "S")

def test_contains_non_string_input_symbol(string_utils):
    with pytest.raises(AttributeError):
        string_utils.contains("SkyPro", None)

    with pytest.raises(TypeError):
        string_utils.contains("SkyPro", 123)

    with pytest.raises(TypeError):
        string_utils.contains("SkyPro", ["S"])


@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_delete_symbol_present(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_substring_present(string_utils):
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_absent(string_utils):
    assert string_utils.delete_symbol("SkyPro", "U") == "SkyPro"

def test_delete_symbol_empty_string(string_utils):
    assert string_utils.delete_symbol("", "a") == ""

def test_delete_symbol_at_start(string_utils):
    assert string_utils.delete_symbol("SkyPro", "S") == "kyPro"

def test_delete_symbol_at_end(string_utils):
    assert string_utils.delete_symbol("SkyPro", "o") == "SkyPr"

def test_delete_multiple_occurrences(string_utils):
    assert string_utils.delete_symbol("SkyProSky", "Sky") == "Pro"

def test_delete_whitespace(string_utils):
    assert string_utils.delete_symbol("Sky Pro", " ") == "SkyPro"

# Негативные тесты
def test_delete_symbol_non_string_input_string(string_utils):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")

    with pytest.raises(AttributeError):
        string_utils.delete_symbol(123, "1")

    with pytest.raises(AttributeError):
        string_utils.delete_symbol(["SkyPro"], "S")

def test_delete_symbol_non_string_input_symbol(string_utils):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol("SkyPro", None)

    with pytest.raises(TypeError):
        string_utils.delete_symbol("SkyPro", 123)

    with pytest.raises(TypeError):
        string_utils.delete_symbol("SkyPro", ["S"])



@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_starts_with_symbol_present(string_utils):
    assert string_utils.starts_with("SkyPro", "S") == True

def test_starts_with_symbol_absent(string_utils):
    assert string_utils.starts_with("SkyPro", "P") == False

def test_starts_with_empty_string(string_utils):
    assert string_utils.starts_with("", "a") == False

def test_starts_with_symbol_at_start(string_utils):
    assert string_utils.starts_with("SkyPro", "S") == True

def test_starts_with_whitespace(string_utils):
    assert string_utils.starts_with(" SkyPro", " ") == True

def test_starts_with_substring(string_utils):
    assert string_utils.starts_with("SkyPro", "Sky") == True

def test_starts_with_case_sensitive(string_utils):
    assert string_utils.starts_with("SkyPro", "s") == False

# Негативные тесты
def test_starts_with_non_string_input_string(string_utils):
    with pytest.raises(AttributeError):
        string_utils.starts_with(None, "a")

    with pytest.raises(AttributeError):
        string_utils.starts_with(123, "1")

    with pytest.raises(AttributeError):
        string_utils.starts_with(["SkyPro"], "S")

def test_starts_with_non_string_input_symbol(string_utils):
    with pytest.raises(TypeError):
        string_utils.starts_with("SkyPro", None)

    with pytest.raises(TypeError):
        string_utils.starts_with("SkyPro", 123)

    with pytest.raises(TypeError):
        string_utils.starts_with("SkyPro", ["S"])



@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_end_with_symbol_present(string_utils):
    assert string_utils.end_with("SkyPro", "o") == True

def test_end_with_symbol_absent(string_utils):
    assert string_utils.end_with("SkyPro", "y") == False

def test_end_with_empty_string(string_utils):
    assert string_utils.end_with("", "a") == False

def test_end_with_symbol_at_end(string_utils):
    assert string_utils.end_with("SkyPro", "o") == True

def test_end_with_whitespace(string_utils):
    assert string_utils.end_with("SkyPro ", " ") == True

def test_end_with_substring(string_utils):
    assert string_utils.end_with("SkyPro", "Pro") == True

def test_end_with_case_sensitive(string_utils):
    assert string_utils.end_with("SkyPro", "O") == False

# Негативные тесты
def test_end_with_non_string_input_string(string_utils):
    with pytest.raises(AttributeError):
        string_utils.end_with(None, "a")

    with pytest.raises(AttributeError):
        string_utils.end_with(123, "1")

    with pytest.raises(AttributeError):
        string_utils.end_with(["SkyPro"], "S")

def test_end_with_non_string_input_symbol(string_utils):
    with pytest.raises(TypeError):
        string_utils.end_with("SkyPro", None)

    with pytest.raises(TypeError):
        string_utils.end_with("SkyPro", 123)

    with pytest.raises(TypeError):
        string_utils.end_with("SkyPro", ["S"])



@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_is_empty_with_empty_string(string_utils):
    assert string_utils.is_empty("") == True

def test_is_empty_with_whitespace_string(string_utils):
    assert string_utils.is_empty("   ") == True

def test_is_empty_with_non_empty_string(string_utils):
    assert string_utils.is_empty("SkyPro") == False

def test_is_empty_with_whitespace_and_text(string_utils):
    assert string_utils.is_empty("   SkyPro") == False

def test_is_empty_with_whitespace_and_empty_string(string_utils):
    assert string_utils.is_empty("   ") == True

def test_is_empty_with_only_tabs(string_utils):
    assert string_utils.is_empty("\t\t\t") == False  # Assuming tabs are not trimmed

def test_is_empty_with_mixed_whitespace(string_utils):
    assert string_utils.is_empty(" \t \n ") == False  # Assuming only leading spaces are trimmed

# Негативные тесты
def test_is_empty_with_non_string_input(string_utils):
    with pytest.raises(AttributeError):
        string_utils.is_empty(None)

    with pytest.raises(AttributeError):
        string_utils.is_empty(123)

    with pytest.raises(AttributeError):
        string_utils.is_empty(["SkyPro"])

def test_is_empty_with_boolean_input(string_utils):
    with pytest.raises(AttributeError):
        string_utils.is_empty(True)

    with pytest.raises(AttributeError):
        string_utils.is_empty(False)



@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_list_to_string_with_integers(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"

def test_list_to_string_with_strings(string_utils):
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"

def test_list_to_string_with_custom_joiner(string_utils):
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

def test_list_to_string_with_empty_list(string_utils):
    assert string_utils.list_to_string([]) == ""

def test_list_to_string_with_single_element_list(string_utils):
    assert string_utils.list_to_string(["Sky"]) == "Sky"

def test_list_to_string_with_numbers_and_strings(string_utils):
    assert string_utils.list_to_string([1, "Sky", 3.5, "Pro"]) == "1, Sky, 3.5, Pro"

# Негативные тесты
def test_list_to_string_with_non_list_input(string_utils):
    with pytest.raises(TypeError):
        string_utils.list_to_string("SkyPro")

    with pytest.raises(TypeError):
        string_utils.list_to_string(123)

    with pytest.raises(TypeError):
        string_utils.list_to_string(None)

def test_list_to_string_with_non_string_joiner(string_utils):
    with pytest.raises(TypeError):
        string_utils.list_to_string(["Sky", "Pro"], 123)

    with pytest.raises(TypeError):
        string_utils.list_to_string(["Sky", "Pro"], None)

    with pytest.raises(TypeError):
        string_utils.list_to_string(["Sky", "Pro"], ["-"])