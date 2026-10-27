PATTERNS = [
    {
        "id":          "countdown_timer",
        "name":        "Fake Countdown Timer",
        "category":    "Interface Interference",
        "severity":    "high",
        "keywords":    [
            "offer expires", "deal ends", "limited time",
            "hurry", "time left", "ends in", "expires soon",
            "sale ends", "offer ends"
        ],
        "explanation": "Creates false urgency — the timer may reset on page reload."
    },
    {
        "id":          "confirmshaming",
        "name":        "Confirmshaming",
        "category":    "Interface Interference",
        "severity":    "high",
        "keywords":    [
            "no thanks i dont want", "no thanks i hate",
            "i prefer paying more", "i love missing out",
            "no i dont want to save", "i like wasting",
            "no thanks i prefer", "i dont want free"
        ],
        "explanation": "Opt-out button uses guilt or shame to discourage the user from declining."
    },
    {
        "id":          "hidden_costs",
        "name":        "Hidden Costs / Drip Pricing",
        "category":    "Sneaking",
        "severity":    "high",
        "keywords":    [
            "service fee", "handling fee", "convenience fee",
            "platform fee", "processing fee", "booking fee",
            "resort fee", "facility charge", "internet handling fee",
            "payment gateway fee", "internet fee"
        ],
        "explanation": "Extra fees are revealed late in the checkout process, after the user has committed."
    },
    {
        "id":          "roach_motel",
        "name":        "Roach Motel / Obstruction",
        "category":    "Obstruction",
        "severity":    "high",
        "keywords":    [
            "cancel subscription", "cancellation policy",
            "unsubscribe", "delete account", "close account",
            "end membership", "stop subscription", "deactivate account"
        ],
        "explanation": "Cancellation is made significantly harder to find and complete than sign-up."
    },
    {
        "id":          "forced_continuity",
        "name":        "Forced Continuity",
        "category":    "Sneaking",
        "severity":    "high",
        "keywords":    [
            "free trial", "trial ends", "after your trial",
            "then per month", "then per year",
            "auto renew", "auto-renew", "auto renewal",
            "automatically charged", "automatically billed",
            "recurring charge", "recurring billing",
            "cancel anytime", "no commitment"
        ],
        "explanation": "Free trial auto-converts to a paid subscription without a clear, prominent warning."
    },
    {
        "id":          "trick_question",
        "name":        "Trick Question / Double Negative",
        "category":    "Interface Interference",
        "severity":    "high",
        "keywords":    [
            "uncheck to not receive", "untick to opt out",
            "deselect to not", "do not uncheck",
            "unsubscribe from not receiving"
        ],
        "explanation": "Confusing double-negative phrasing is designed to produce the opposite of the user's intended response."
    },
    {
        "id":          "privacy_zuckering",
        "name":        "Privacy Zuckering",
        "category":    "Forced Action",
        "severity":    "high",
        "keywords":    [
            "share with partners", "share with third parties",
            "personalised ads", "personalized ads",
            "targeted advertising", "we may share your data",
            "marketing purposes", "share your information with"
        ],
        "explanation": "Data sharing is buried in consent flows and defaults to maximum sharing without clear disclosure."
    },
    {
        "id":          "fake_scarcity",
        "name":        "False Scarcity",
        "category":    "Social Engineering",
        "severity":    "medium",
        "keywords":    [
            "only left", "selling fast", "almost gone",
            "last one", "in high demand", "people are looking",
            "others are viewing", "limited availability",
            "few remaining", "going fast"
        ],
        "explanation": "Creates an artificial sense of scarcity to pressure the user into a quick decision."
    },
    {
        "id":          "fake_social_proof",
        "name":        "Fake Social Proof",
        "category":    "Social Engineering",
        "severity":    "medium",
        "keywords":    [
            "people viewing", "watching this", "bought today",
            "recently purchased", "trending now",
            "popular right now", "others are looking",
            "people looking at this", "booked today"
        ],
        "explanation": "Unverifiable claims about other users' behaviour are used to pressure purchasing decisions."
    },
    {
        "id":          "pre_checked",
        "name":        "Pre-Selected Options",
        "category":    "Sneaking",
        "severity":    "medium",
        "keywords":    [
            "yes send me", "yes i want", "keep me updated",
            "yes add", "include me", "opt me in",
            "i agree to receive", "sign me up for offers"
        ],
        "explanation": "Options are pre-ticked by default, placing the burden of opting out on the user."
    },
    {
        "id":          "forced_account",
        "name":        "Forced Account Creation",
        "category":    "Forced Action",
        "severity":    "medium",
        "keywords":    [
            "create account to continue", "sign up to view",
            "register to access", "login required to",
            "must sign in", "account required",
            "create an account to", "sign in to continue"
        ],
        "explanation": "Access to content or a service is gated behind mandatory account registration."
    },
    {
        "id":          "nagging",
        "name":        "Nagging / Persistent Upsell",
        "category":    "Nagging",
        "severity":    "low",
        "keywords":    [
            "upgrade now", "try premium", "get premium",
            "upgrade to", "unlock all features", "go premium",
            "subscribe now", "start free trial",
            "unlock premium", "upgrade your plan"
        ],
        "explanation": "Repeated prompts to upgrade or subscribe appear even after the user has previously declined."
    },
]