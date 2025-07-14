from django.utils.text import slugify
from django.utils.crypto import get_random_string


def auto_generate_slug():
    # Generate slug if it's not already set or if the title changes
    base_slug = slugify("first_title")
    unique_slug = base_slug
    counter = 1
    unique_slug = f"{base_slug}-{get_random_string(6)}"  # Add a random string for uniqueness
    counter += 1

    new_slug = unique_slug

    return new_slug
