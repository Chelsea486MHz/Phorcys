#
# Build image
#
FROM python:3.12-slim AS image-build

RUN apt update
RUN apt install -y --no-install-recommends \
    build-essential \
    gcc
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy Phorcys source
COPY requirements.txt .
COPY ./phorcys/. /phorcys/
COPY pyproject.toml .
COPY setup.cfg .

# Install build-time deps
RUN pip install setuptools wheel build

# Install Phorcys deps
RUN pip install --no-cache-dir -r requirements.txt

# Build Phorcys
RUN python -m build

# Install Phorcys
RUN pip install --no-cache-dir dist/*.whl



#
# Production image
#
FROM python:3.12-slim AS image-prod

# Container settings
ENV APP_USER 'phorcys'
ENV APP_DIR '/home/phorcys'

# App settings
ENV DEBUG False
WORKDIR $APP_DIR
USER $APP_USER

# Python security
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR 1

# Install venv from the build image
COPY --from=image-build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"