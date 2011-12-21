from os.path import dirname, abspath, join

BASE_PATH = dirname(__file__)
ROOT_PATH = abspath(dirname(join(BASE_PATH, '../')))

MEDIA_ROOT = join(ROOT_PATH, 'static')
SITE_ROOT = ROOT_PATH
STATICFILES_DIRS = (
  join(ROOT_PATH, 'static'),
)

REDIR = '' #URL used for redirection? who knows?
