FROM openresty/openresty:alpine-fat

RUN luarocks install lua-resty-openidc
RUN luarocks install lua-resty-session

COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf