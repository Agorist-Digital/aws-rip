from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="cleghornw@protonmail.com",
    author_name="William Cleghorn",
    cdk_version="2.1.0",
    module_name="aws_rip",
    name="aws-rip",
    poetry=True,
    version="0.1.0",
)

project.synth()