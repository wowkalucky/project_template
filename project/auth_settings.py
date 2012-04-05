
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = [
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.vkontakte.VKontakteOAuth2Backend',
]

AUTHENTICATION_BACKENDS = SOCIAL_AUTH_AUTHENTICATION_BACKENDS + [
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_ENABLED_BACKENDS = ('twitter', 'facebook', 'vkontakte-oauth2')

LOGIN_ERROR_URL = '/profile/details/'
LOGIN_REDIRECT_URL = '/profile/details/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

TWITTER_CONSUMER_KEY         = '2FGRLJi5PdF5jtVJOgT9Hg'
TWITTER_CONSUMER_SECRET      = 'gCRpX8uuA51FNzKY6a3i36pJINHg4ztLenYUMAc2hE'
FACEBOOK_APP_ID              = '316098028425892'
FACEBOOK_API_SECRET          = '5b40fb8bac625c0fc8a4beba97d0fea3'
VKONTAKTE_APP_ID             = '2786037'
VKONTAKTE_APP_SECRET         = '3rhSxvmnbjwkUe1Eamw7'
