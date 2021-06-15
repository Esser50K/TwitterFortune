# Twitter Fortune

This is a very simple bot that uses the `fortune` command line tool to generate tweets.

You can pass your secrets as environment variables to your docker container.

You can also use the `OFFENSIVE` environment key to use `fortune` in offensive mode. USE AT OWN DISCRETION.

Complete example:

```
docker build -t twitter_fortune:latest .
docker run -d -e OFFENSIVE=True \
              -e TWITTER_API_KEY=<YOUR_API_KEY> \
              -e TWITTER_SECRET_KEY=<YOUR_TWITTER_SECRET_KEY> \
              -e TWITTER_ACCESS_TOKEN=<YOUR_TWITTER_ACCESS_TOKEN> \
              -e TWITTER_ACCESS_TOKEN_SECRET=<YOUR_TWITTER_ACCESS_TOKEN_SECRET> \
              twitter_fortune
```