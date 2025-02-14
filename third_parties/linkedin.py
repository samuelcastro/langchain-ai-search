import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/samuelcastro/afafea0032854ab53d647edc05683435/raw/3bcb3cf3cfeb52baa0f7e3e2e3ecae47a2790b55/sam-silva-data.json"
        response = requests.get(linkedin_profile_url, timeout=10)
        data = response.json()
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.getenv("SCRAPIN_API_KEY"),
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, timeout=10)
        data = response.json().get("person", {})  # Use empty dict as fallback

    # Create a new dictionary by filtering out empty/null values and specific keys
    # - Removes any values that are empty lists, empty strings, or None
    # - Excludes the keys "peopleAlsoViewed" and "certifications"
    # This cleans up the LinkedIn profile data to only include meaningful information
    cleaned_data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["peopleAlsoViewed", "certifications"]
    }
    return cleaned_data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/samuelcasilva/", mock=True
        )
    )
