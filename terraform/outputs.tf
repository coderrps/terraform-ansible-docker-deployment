# output "ec2_public_ip" {
#   value = aws_instance.portfolio_server.public_ip
# }

# output "ec2_public_dns" {
#   value = aws_instance.portfolio_server.public_dns
# }

output "ec2_public_ips" {
  value = aws_instance.portfolio_server[*].public_ip
}

output "ec2_public_dns" {
  value = aws_instance.portfolio_server[*].public_dns
}