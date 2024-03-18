FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=pwd
ENV MYSQL_DATABASE=storefront
ENV MYSQL_USER=zmakhkha
ENV MYSQL_PASSWORD=my_password

# Copy the SQL script into the Docker container
COPY ./data.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3306