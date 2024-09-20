look for `HFLA note:` for notes

prerequisites needs a new title and the template needs real prerequisites 
### intro
We are looking forward to having you on our team. Please ensure you have prior experience with the HfLA website team before contributing to our repository.
### features
 - special instructions for windows included
### prerequisites 
- [x] join
    - [x] `added hyperlinks for ease` ops [Slack Channel](https://app.slack.com/client/T04502KQX/CGRATJCCF)
    - [x] `added hyperlinks for ease` [devops-security](https://github.com/hackforla/devops-security) repository
### Action Items
- [x] Add this issue to the Project Board under the Projects section (gear in right side panel). # add [CoP: DevOps: Project Board](https://github.com/orgs/hackforla/projects/73)
> - [x] Add this issue to the Project Board under the Projects section (gear in right side panel). as title [CoP: DevOps: Project Board](https://github.com/orgs/hackforla/projects/73)
- [x] Attend weekly team meeting, Wednesdays 6-8pm PST.
  - Note: There are no meetings on the 1st-7th of every month. # should be attention getting instead of a step
        <ins>***Note: There are no meetings on the 1st-7th of every month.***</ins>

### AWS 
- [x] for the following watch video guide [Getting Started With AWS Cloud | Step-by-Step Guide](https://www.youtube.com/watch?si=78GhlDLV5zZu8qwh&v=CjKhQoYeR4Q&feature=youtu.be)  
  - [X] create MFA for ROOT
  - [x] Complete [Creating a personal AWS account](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#creating-a-personal-aws-account)
    - [x] `HFLA note: link was broken` [Login as root user & setup MFA](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#login-as-root-user--setup-mfa)
    - [x] `HFLA note: link led to creating iam user group not user` [Creating an IAM User](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#login-as-root-user--setup-mfa)

### AWS IAM new user
^ part of [Getting Started With AWS Cloud | Step-by-Step Guide](https://www.youtube.com/watch?v=CjKhQoYeR4Q)
  - [X] create admin user
    - [X] click users category on left 
    - [X] click add user
    - [X] enter username
    - [X] click "Provide user access to the AWS Management Console - optional"
    - [X] select "create IAM user"
    - [X] click "custom password"
    - [X] enter password
    - [X] unclick "Users must create a new password at next sign-in - Recommended"
    - [X] click next
    - [X] click "Attach policies directly"
    - [X] only check "AdministratorAccess"
    - [X] click "next"
    - [X] click "create user"
    - [X] save "Console sign-in URL" to bookmark for easy access
    - [X] sign in to new admin user

### AWS CLI
```bash
HFLA note: maybe this process can be skipped using the following code in cloudshell or local
aws iam create-user --user-name drakeredwind01
aws iam create-login-profile --user-name drakeredwind01 --password Black2BlackHFLA
aws iam create-access-key --user-name drakeredwind01 > drakeredwind01_access_key.json
nano drakeredwind01_access_key.json
```
^ part of [Getting Started With AWS Cloud | Step-by-Step Guide](https://www.youtube.com/watch?v=CjKhQoYeR4Q)
- [X] go to [AWS CLI](https://aws.amazon.com/cli/)
- [X] click "getting started" (under the big "1")
- [X] SideNav click Get started > [Install/Update](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
`HFLA note: I had to do this part again. i did it before but the aws commands weren't working on my computer`
- [X] for windows
  - [X] in CMD run the following:
    - [X] msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
    - [X] confirm the installation by running:
    - [X] aws --version
    - [X] for instance mine said "aws-cli/2.17.39 Python/3.11.9 Windows/10 exe/AMD64"
- [X] link AWS CLI with your account
  - [X] go to IAM > [Security credentials](https://us-east-1.console.aws.amazon.com/iam/home?region=us-west-2#/security_credentials)
  - [X] click "create Access key"
  - [X] click "use case" > "Command Line Interface (CLI)"
  - [X] click "I understand the above recommendation and want to proceed to create an access key."
  - [X] click "next"
  - [X] click "create access key"
  - [X] save your "Access key" and "Secret access key"
  - [X] check to see it worked by using CMD to enter:
  - [X] aws
  - [X] configure it:
    - [X] enter into cmd: "aws configure"
    - [X] enter your "Access key" you saved
    - [X] enter your "Secret access key" you saved
    - [X] enter "Default region name" "us-west-2"
    - [X] enter "Default output format" "json"
    - [X] check to see it worked
    - [X] enter: "aws s3 ls"
    - [X] optional: for more commands you can go to [Use the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-using.html)
    - [X] optional: save the above link in bookmarks
  - [X] in CMD run following:
    - [X] aws iam create-group --group-name AdminGroup
    - [X] aws iam add-user-to-group --group-name AdminGroup --user-name HFLA
    - [X] aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --group-name AdminGroup




`HFLA note: maybe replace?`
- [x] Read and follow the instructions in [Setting up IAM and AWS CLI](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#setting-up-iam-and-aws-cli) for:
    - [x] [Creating an IAM Group](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#create-an-iam-group)
    - [x] [Attaching IAM user to IAM Group](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#attach-iam-user-to-iam-group)
    - [x] [Providing `AdministratorAccess` policy to IAM group](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#attach-administratoraccess-policy-to-iam-group)
    - [x] Log in as the newly created user instead of continuing to log in as the root user (it is not recommended to login with root access).
    - [x] [Generating user access keys](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#generating-access-keys-for-aws-cli)

### AWS CLI quick quide
```bash
aws iam create-group --group-name AdminGroup
aws iam create-user --user-name drakeredwind01
aws iam create-login-profile --user-name drakeredwind01 --password Black2BlackHFLA
aws iam add-user-to-group --group-name AdminGroup --user-name drakeredwind01
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --group-name AdminGroup
aws iam create-access-key --user-name drakeredwind01 > drakeredwind01_access_key.json
nano drakeredwind01_access_key.json
```


- `HFLA note: maybe remove?` [x] Complete the instructions in [AWS Documentation](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html) and choose your operating system to install AWS CLI. 
- `HFLA note: maybe remove?` [x] Complete the instruction in [AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-short-term.html) to setup the AWS CLI.

### `old`backend state
- [x] Read follow the instructions in [Creating a backend state](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#creating-backend-state).
- [x] Create S3 bucket
  - [x] Region: us-west-2 (Oregon) 
  - [x] Name: `hfla-ops-terraform-state` 
  - [x] Enable versioning 
  - [x] Enable server-side encryption
- [x] Set up DynamoDB to store backend
  - [x] Create table `hfla_ops_terraform_table`
  - [x] Set partition key to `LockID` with a type of `String`
  - [x] Choose on-demand capacity

aws s3api put-bucket-encryption --bucket drakeredwind01-hfla-ops-terraform-state --server-side-encryption-configuration '{
    "Rules": [
        {
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "AES256"
            }
        }
    ]
}'



### Resources/Instructions
https://developer.hashicorp.com/terraform/language/settings/backends/s3


### `new`backend state
- [x] Read follow the instructions in [Creating a backend state](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#creating-backend-state).
- [x] Create S3 bucket
  - [x] `added for ease` search for `s3`
  - [x] AWS Region: US West (Oregon) us-west-2
  - [x] `?` Bucket type `General purpose` or `Directory - New`
  - [x] Bucket name `hfla-ops-terraform-state`
  - [x] Enable versioning 
  - [x] `?` Enable server-side encryption
    - [x] `?` Server-side encryption with Amazon S3 managed keys (SSE-S3)
    - [x] `?` Server-side encryption with AWS Key Management Service keys (SSE-KMS)
  - [x] `?` Bucket Key `default Enable` 
- [x] Set up DynamoDB to store backend
  - `added for ease` search for `DynamoDB`
  - `added for ease` Table details
    - [x] Create table `hfla_ops_terraform_table`
    - [x] Set partition key to `LockID` with a type of `String`
    - [x] Choose on-demand capacity
  - `added for ease` Table settings
    - [x] `added` Customize settings
  - `added for ease` Read/write capacity settings
    - [x] On-demand
  - `?` Deletion protection




### Terraform
- [x] Install Terraform locally by following the instructions of the installation guide mentioned in [Installing Terraform](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#installing-terraform)
    - (windows) **make sure terraform is in your path**
- [x] Install Terraform Docs locally by following the instructions of the installation guide mentioned in [Installing Terraform docs](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#installing-terraform-docs)
  #### WINDOWS
  - if you have windows you first need [scoop](https://scoop.sh/#/)
  - run scoop command
    - ```cmd
      scoop bucket add terraform-docs https://github.com/terraform-docs/scoop-bucket
      scoop install terraform-docs
      ```
    - if you don't have scoop run install it by running the following in powershell
      - ```powershell
        iex (new-object net.webclient).DownloadString('https://get.scoop.sh')
        ```
      - if you get following error in red letters run the bellow command `PowerShell requires an execution policy in [Unrestricted, RemoteSigned, ByPass] to run Scoop. For example, to set the execution policy to 'RemoteSigned' please run 'Set-ExecutionPolicy RemoteSigned -Scope CurrentUser'.`
        - ```powershell
          Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
          ```
- [x] Complete the instructions in [Clone the repository](https://github.com/hackforla/devops-security/blob/main/CONTRIBUTING.md#clone-the-repository)
- [x] Submit a [new request](https://github.com/hackforla/devops-security/issues/new?assignees=&labels=enhancement&projects=&template=request-aws-iam-resources.yml) to create new AWS user account and then self-assign this issue.
  - [x] `? {github handle} or {service account}. which service account? the one for aws?` Account Name: 
  - [x] Project(s) Name: https://github.com/hackforla/devops-security.git
  - [x] `? no instructions given. should i put in: in order to complete "Pre-work Checklist: DevOps-Security-Member: drakeredwind01 #36"` Reason for access:






- [x] Create a new branch from main by executing the command
    ```bash
    git checkout -b issue-number-add-new-iam-user
    ```
    - `added for ease` example
        ```bash
        git checkout -b 36-add-new-iam-user-drakeredwind01
        ```

`HFLA note: potentialy deprecated (unsure if you should add a user)`
- [x] Navigate to the `aws-user.tf` file and add your user information and follow the below template.

    ```bash
    module "iam_user_testiamuser" {
    source = "./modules/aws-users"
    
    user_name = "testiamuser"
    user_tags = {
      "Project"      = "devops-security"
      "Access Level" = "1"
    }
    user_groups = ["read-only-group"]
    }
    ```
    example
    ```bash
        module "iam_user_drakeredwind01" {
          source = "./modules/aws-users"
        
          user_name = "drakeredwind01"
          user_tags = {
            "Project"      = "devops-security"
            "Access Level" = "1"
          }
          user_groups = ["read-only-group"]
        }
    ```
- [x] In your code editor navigate to `terraform` directory. `cd terraform`

<br>
<br>
<br>
<br>
<br>


# [left off](https://github.com/hackforla/devops-security/issues/36)
- [x] Execute the command `terraform init` to initialize terraform in the directory. Address any failures that arise (if any).
    - if using pycharm go to `settings` then `plugins`  
      - [x] install `AWS Core`
      - [x] install `AWS Toolkit`
      - [x] restart pycharm
          - on the left side bar you will see `project`,`commit`,`pull request`,`structure`,`AWS Toolkit`
      - [x] click `AWS Toolkit`
      - [x] click `Add Another Connection`
      - [x] click `IAM Credentials`
      - [x] click `Continue`
      - [x] enter `profile name`,`access key`,`secret key` found in `access_key.json`
          - go to [cloudshell](https://us-west-2.console.aws.amazon.com/cloudshell) and type `nano access_key.json`
      - [x] click `Continue`
    - if after input `terraform init` get message 
      ```
        ╷
        │ Error: validating provider credentials: retrieving caller identity from STS: operation error STS: GetCallerIdentity, https response error StatusCode: 403, RequestID: 38c7ba80-a5e4-4a1b-bf31-589bb74b8f4a, api error InvalidClientTokenId: The security token included in the request is invalid.
        │ 
        │ 
        ╵
      ```
        ### Configure the AWS CLI with IAM Identity Center authentication
          from https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html#cli-configure-sso-prereqs
            - (Recommended) SSO token provider configuration.
              if you do not have established access through IAM Identity Center
              - #### Get started with common tasks in IAM Identity Center

### Configure the AWS CLI with IAM Identity Center authentication
  from https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html#cli-configure-sso-prereqs
    - (Recommended) SSO token provider configuration.
      if you do not have established access through IAM Identity Center
### Get started with common tasks in IAM Identity Center



### extra THE BLOCKER DESTROYED
put in cloud shell
    ```
    aws dynamodb create-table \
        --table-name hfla_ops_terraform_table \
        --attribute-definitions AttributeName=LockID,AttributeType=S \
        --key-schema AttributeName=LockID,KeyType=HASH \
        --billing-mode PAY_PER_REQUEST
    ```
if `.terraform` file does not have providers
    delete `.terraform`
    run `terraform init --backend-config=backend.tfvars`






- [x] Execute the command `terraform plan` this will output a plan replicating the same IAM resources as the devops security account. Address any failures that arise (if any).
- [x] Then execute the command `terraform apply -auto-approve` this will create all of the resources that are currently managed by Devops Security. All of the resources created here incur zero cost except for the Dynamo DB installation, which should remain in the free tier.
      - [x] ** If you have cost concerns, Run a Terraform Destroy to take down all of the resources you created (don't worry, you can recreate them just as quickly). **
`HFLA note: how to test your changes as mentioned below`
- [x] Once you have tested your changes, stage them in git with 
    - [x] add your profile to `aws-users.tf`
    - [x] `git status` command.
    - [x] then `git add path/to/file/aws-users.tf` (you can copy from above output for the file path).
    - [x] make sure you added it by using `get status` again
- [x] Commit the changes by executing `git commit -m "briefly describing the changes"`.
- [x] example `git commit -m "drakeredwind01 added to aws-users.tf"`.
- [x] Push the changes with `git push --set-upstream origin name-of-branch`
- [x] example `git push --set-upstream origin git push --set-upstream origin 36-add-new-iam-user-drakeredwind01`



aws services customer care center




<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>














<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


# NOTES
my notes

python "D:\documents\ai\python\my-first-conda-project\_read to me args (with read time and csv stats) 1.py" "

commenter:drakeredwind01

suggest removing `needs-triage` `needs-sig` and adding `triage/accepted`, `sig-network`, and `sig-security`

## O3DE Network SIG - Issue Triage Guide
https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-triage+-label%3Asig%2Fnetwork++--label%3Asig%2Fbuild+--label%3Asig%2Fbuild+

1. Open issues with `needs-sig` label: https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-sig
   1. `OLD` 
   2. `NEW` 
2. Main O3DE repository: 
   1. `OLD` https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-triage+label%3Asig%2Fnetwork
   2. `NEW` https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-triage+-label%3Asig%2Fnetwork++--label%3Asig%2Fbuild+--label%3Asig%2Fbuild+
>     altered is:issue is:open label:needs-triage label:sig/network
>      to     is:issue is:open label:needs-triage -label:sig/network  -label:sig/build -label:sig/build  
3. Multiplayer Sample: https://github.com/o3de/o3de-multiplayersample/labels/needs-triage
   1. `OLD` 
   2. `NEW` 
4. NetSoak Test: https://github.com/o3de/o3de-netsoaktest/issues
   1. `OLD` 
   2. `NEW` 
5. [Multiplayer template](https://github.com/o3de/o3de-extras/tree/development/Templates/Multiplayer) issues in: 
   1. `OLD` issues in: https://github.com/o3de/o3de-extras/labels/sig%2Fnetwork
   2. `NEW` issues in: https://github.com/o3de/o3de-extras/issues?q=is%3Aopen+label%3Asig%2Fnetwork+++-label%3Asig%2Fnetwork+-label%3Asig%2Fcore+-label%3Asig%2Fbuild+-label%3Asig%2Fsimulation+-label%3Asig%2Frelease+-label%3Asig%2Fgraphics-audio+-label%3Asig%2Fplatform+
>     altered is:open label:sig/network  -label:sig/network
>      to      is:open label:sig/network   -label:sig/network -label:sig/core -label:sig/build -label:sig/simulation -label:sig/release -label:sig/graphics-audio -label:sig/platform  





## O3DE sig-security - Issue Triage Guide
https://github.com/o3de/sig-security/blob/main/TRIAGE_GUIDE.md

* O3DE issues to triage for SIG:
    * https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-triage+label%3Asig%2Fsecurity
    * https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-triage+-label%3Asig%2Fsecurity+-label%3Asig%2Fbuild+-label%3Asig%2Fcontent+-label%3Asig%2Fcore+-label%3Asig%2Fdocs-community+-label%3Asig%2Fnetwork+-label%3Asig%2Fplatform+-label%3Asig%2Fgraphics-audio+-label%3Asig%2Frelease+-label%3Asig%2Fsimulation+-label%3Asig%2Ftesting+-label%3Asig%2Fui-ux+-label%3Asig%2FTAC%2FTSC+-label%3Asig%2Fmobile+
* O3DE known security issues: https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Akind%2Fsecurity
    * https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Akind%2Fsecurity
    * https://github.com/o3de/o3de/issues?q=is%3Aissue+is%3Aopen+label%3Akind%2Fsecurity+-label%3Atriage%2Faccepted+-kind%3Akind%2Fsecurity
* Dependabot alerts to check (link only accessible to SIG-Security maintainers): 
  <br>`broken` https://github.com/o3de/o3de/security/dependabot
    * For new alerts, create new GitHub issues against [O3DE](https://github.com/o3de/o3de) and tag with `kind\security` label for tracking.
    * **WARNING**: Since the O3DE _python/requirements.txt_ file includes hashes, Dependabot-generated PRs against this file should be **manually tested** against a clean `/python` folder (that is, no `/runtime` child dir) **prior to merging** in order to suss out any issues with hashing transitive dependencies.







