FROM dirichlet/basic-vim

# Get my vim config
RUN git clone https://github.com/evermax/dotvim.git /root/.vim

RUN cd /root/.vim && chmod +x setup.sh && ./setup.sh basic

# Install all vim plugins
RUN vim +PluginInstall +qall
