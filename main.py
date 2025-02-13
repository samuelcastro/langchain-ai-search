from agents.linkedin_lookup_agent import lookup

if __name__ == "__main__":
    linkedin_profile_url = lookup(name="Sam Silva")
    print(linkedin_profile_url)
