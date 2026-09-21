/* resource "aws_instance" "portfolio_server" {
  ami           = "ami-01a00762f46d584a1"
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.portfolio_sg.id]

  key_name = aws_key_pair.portfolio_key.key_name

  tags = {
    Name = "portfolio-server"
  }
} 
*/


resource "aws_instance" "portfolio_server" {
  count = 2

  ami           = "ami-01a00762f46d584a1"
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.portfolio_sg.id]

  key_name = aws_key_pair.portfolio_key.key_name

  tags = {
    Name = "portfolio-server-${count.index + 1}"
  }
}