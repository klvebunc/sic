default_app_config = "sic.apps.SicAppConfig"


BANNED_USERNAMES = [
    "admin",
    "administrator",
    "contact",
    "fraud",
    "guest",
    "help",
    "hostmaster",
    "sic",
    "Cher",
    "mailer-daemon",
    "moderator",
    "moderators",
    "nobody",
    "postmaster",
    "root",
    "security",
    "support",
    "sysop",
    "webmaster",
    "enable",
    "new",
    "signup",
]

# days old accounts are considered new for
NEW_USER_DAYS = 70

# minimum karma required to be able to offer title/tag suggestions
MIN_KARMA_TO_SUGGEST = 10

# minimum karma required to be able to flag comments
MIN_KARMA_TO_FLAG = 50

# minimum karma required to be able to submit new stories
MIN_KARMA_TO_SUBMIT_STORIES = -4

# minimum karma required to process invitation requests
MIN_KARMA_FOR_INVITATION_REQUESTS = MIN_KARMA_TO_FLAG

# proportion of posts authored by user to consider as heavy self promoter
HEAVY_SELF_PROMOTER_PROPORTION = 0.51

# minimum number of submitted stories before checking self promotion
MIN_STORIES_CHECK_SELF_PROMOTION = 2