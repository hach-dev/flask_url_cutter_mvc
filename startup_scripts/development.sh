echo "STARTING LOCAL DEVELOPMENT"
# --reload allows developers to update files locally, and the container/browser updates automatically.
# --spew gives debug logging on everything happening in dev.
# For more infor on gunnicorn configs: https://docs.gunicorn.org/en/stable/settings.html
# About unicorn https://www.uvicorn.org/deployment/

# https://pgjones.gitlab.io/hypercorn/

cd src/main
flask run