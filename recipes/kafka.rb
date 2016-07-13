include_recipe 'datadog::dd-agent'

# Monitor Kafka
#
# Assuming you have 2 clusters "test" and "prod",
# one with and one without authentication
# you need to set up the following attributes
# node.datadog.kafka.instances = [
#   {
#     :host => "localhost",
#     :port => "9999",
#     :name => "prod",
#     :user => "username",
#     :password => "secret"
#   },
#   {
#     :host => "localhost",
#     :port => "8199",
#     :name => "test"
#   }
# ]

datadog_monitor 'kafka' do
  instances node['datadog']['kafka']['instances']
  action :add
  notifies :restart, 'service[datadog-agent]' if node['datadog']['agent_start']
end
