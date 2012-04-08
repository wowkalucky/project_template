
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = [
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
]

AUTHENTICATION_BACKENDS = SOCIAL_AUTH_AUTHENTICATION_BACKENDS + [
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'google-oauth',)

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

LOGIN_ERROR_URL = '/profile/details/'
LOGIN_REDIRECT_URL = '/profile/details/'

SOCIAL_AUTH_RAISE_EXCEPTIONS = False

FACEBOOK_APP_ID              = '316098028425892'
FACEBOOK_API_SECRET          = '5b40fb8bac625c0fc8a4beba97d0fea3'
GOOGLE_CONSUMER_KEY          = '715675164878.apps.googleusercontent.com'
GOOGLE_CONSUMER_SECRET       = 'sokcgayZtiUxesJJO2JyQoJ9'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'project.pipeline.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',

)
