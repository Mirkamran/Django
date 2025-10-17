# Use official NGINX image
FROM nginx:alpine

# Remove default NGINX HTML files
RUN rm -rf /usr/share/nginx/html/*

# Copy your custom HTML files into the container
COPY index.html /usr/share/nginx/html/

# Expose port 80 for web traffic
EXPOSE 80

# Start NGINX (default command from base image)
CMD ["nginx", "-g", "daemon off;"]
