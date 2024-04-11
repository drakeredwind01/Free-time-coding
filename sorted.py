secops = ["Analytics and data", "Balancers", "DNS", "Load", "Network agility", "Orchestration and automation",
          "Security", "Single Source of Truth (SOT)", "configuration", "monitoring", "provisioning",
          "troubleshooting", ]
for item in sorted(set([item.title() for item in secops])):
    print(item)
