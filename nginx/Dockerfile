FROM nginx


# Define the environment variables

ENV PORT 8089


# Install optional dependencies

RUN apt-get update

RUN apt-get install wget -y

RUN apt-get install curl -y


# Run the commands to alter the files in the nginx server

RUN rm -rf /etc/nginx/conf.d/

RUN rm /etc/nginx/nginx.conf

RUN mkdir /etc/nginx/sites-enabled


COPY conf.d /etc/nginx/conf.d

COPY nginx.conf /etc/nginx/nginx.conf

COPY python_blue.conf /etc/nginx/sites-available/python_blue.conf

COPY python_green.conf /etc/nginx/sites-available/python_green.conf


# RUN ln -s /etc/nginx/sites-available/python_blue.conf /etc/nginx/sites-enabled/python_blue.conf

# RUN ln -s /etc/nginx/sites-available/python_green.conf /etc/nginx/sites-enabled/python_green.conf


CMD ["nginx", "-g", "daemon off;"]

EXPOSE $PORT
