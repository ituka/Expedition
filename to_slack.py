import slackweb

tmp = input("何？")

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text="%s" %(tmp))
