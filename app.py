import os
from aws_cdk import App, Environment
from aws_rip.main import RIP

# for development, use account/region from cdk cli
dev_env = Environment(
  account=os.getenv('CDK_DEFAULT_ACCOUNT'),
  region=os.getenv('CDK_DEFAULT_REGION')
)

app = App()
RIP(app, "aws-rip-dev", env=dev_env)
# MyStack(app, "aws-rip-prod", env=prod_env)

app.synth()
