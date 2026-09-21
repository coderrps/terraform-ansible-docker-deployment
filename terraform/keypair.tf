resource "aws_key_pair" "portfolio_key" {
  key_name   = "portfolio-key"
  public_key = file("C:/Users/RITU PRIYA SINGH/Downloads/portfolio-key.pub")
}