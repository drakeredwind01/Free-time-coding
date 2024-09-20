# zz Pre-work Checklist DevOps-Security-Member drakeredwind01 #36
20240626T182821Z
<br>Work through this template
https://github.com/hackforla/devops-security/issues/36

Made from Issue: Pre-work Template - DevOps-Security
Add comments as working through template
Ask questions here:
Questions / Answers from ops members #93
https://github.com/hackforla/ops/issues/93

Slack ops channel
https://app.slack.com/client/T04502KQX/CV7QGL66B


## issue and possible solutions
```
My problem
I get error 
╷
│ Error: Required plugins are not installed
│
│ The installed provider plugins are not consistent with the packages selected in the dependency lock file:
│   - registry.terraform.io/hashicorp/aws: there is no package for registry.terraform.io/hashicorp/aws 5.34.0 cached in .terraform\providers
│
│ Terraform uses external plugins to integrate with a variety of different infrastructure services. To download the
│ plugins required for this configuration, run:
│   terraform init
╵
```
I think the important part is:
>│   - registry.terraform.io/hashicorp/aws: there is no package for registry.terraform.io/hashicorp/aws 5.34.0 cached in .terraform\providers

Possible solution:
```
https://github.com/gruntwork-io/terragrunt/issues/1960
It seems they fixed this by deleting “.terraform.lock.hcl”

Can confirm removing the lock files solves it, but you need to do it on the current module and any it depends on.
terragrunt version v0.36.1
Terraform v1.1.5
on darwin_amd64

Itsayellow says:
He also had this issue and deleting the terraform lock files but that wasn't helping.
But “Finally I found if I deleted ./.terragrunt-cache from where I was executing terragrunt, it finally worked without error for me.”
```
Extra advice:
```
luogedai commented on Jan 13, 2022
If you have dependencies, try to clear and init or upgrade the dependencies first. This step solved my issue.
```

## AWS support
[connectria](https://www.connectria.com/landing/aws/?utm_medium=cpc&utm_source=google&utm_campaign=[Oct2023]Amazon-AWS&utm_ad_group=AWS-Partners&keyword=aws%20partners&utm_campaign=%5BOct+2023%5D+Amazon+-+AWS&utm_medium=ppc&utm_term=aws%20partners&utm_source=adwords&hsa_grp=157955541521&hsa_acc=5815648820&hsa_tgt=kwd-22077665129&hsa_kw=aws%20partners&hsa_src=g&hsa_mt=b&hsa_cam=20624982663&hsa_ver=3&hsa_ad=676351969839&hsa_net=adwords&gad_source=1&gclid=CjwKCAjw3P-2BhAEEiwA3yPhwGijL5cI2LIx2FpvAN8NhDjj9tQX-dFxhNyTbNU2LxzK1il1KpMi-hoCeY0QAvD_BwE)
possible aws support through 3rd party (still waiting for them to get back to me)
```
connectria.com
A dedicated team of AWS experts, available 24/7.
Markus will leave number for sales team to see if we can have a small consultation fee for help
```


AWS Support plans
```
https://us-east-1.console.aws.amazon.com/support/plans/home#/
https://aws.amazon.com/premiumsupport/pricing/ 
```
