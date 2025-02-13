from agents.twitter_lookup_agent import lookup

if __name__ == "__main__":
    linkedin_profile_url = lookup(name="Elon Musk")
    print(linkedin_profile_url)
