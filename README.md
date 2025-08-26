# NadinSoft DevOps Pre-Interview Task

## Overview
This repository contains a containerized Python web service with complete CI/CD pipeline, monitoring, and networking configurations as part of a DevOps practical assessment.

## Architecture
- **Application**: Simple Python web service (django)
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitLab CI/CD pipeline
- **Monitoring**: Prometheus & Alertmanager
- **Visualization**: Grafana dashboards
- **High Availability**: Container restart policies



## Prerequisites
- Docker (version 20.10+)
- Docker Compose (version 2.0+)
- Git
- GitLab server


## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd nadinsoft-devops
```


### 3. Local Development Setup
```bash
# Build and start all services
docker compose up -d

# Verify services are running
docker compose ps

```

### 4. Access Services
(NOTE : I've used 9091 and 9095 ports for Prometheus and Grafana , because the traiditional ports (9090 and 9093) were used by gitlab internal service)

- **Web Application**: http://localhost:8000
- **Prometheus**: http://localhost:9091
- **Grafana**: http://localhost:3000
- **Alertmanager**: http://localhost:9095

## CI/CD Pipeline

### Pipeline Stages
1. **Build**: Create Docker images
2. **Test**: Run unit tests
3. **Push**: Push to container registry
4. **Deploy**: Deploy to production

### Triggering the Pipeline

#### Automatic Triggers
- **Push to main**: Full pipeline (build → test → deploy to production)
- **Push to develop**: Build and test only
- **Merge requests**: Build, test, and deploy




## Monitoring & Alerting

### Prometheus Metrics
- **Application metrics**: Request count, response time


### Grafana Dashboards
- **Application Overview**: Request metrics and performance

### Alert Rules
- High response time (95% of requests are taking more than 0.5 seconds)  
- Service unavailable (The Django app has been unreachable for 10+ seconds)

## Security & Networking

### iptables Configuration
```bash
# Apply iptable rules
sudo ./setup-iptables.sh

# Verify rules
sudo iptables -L -n -v

# Test external access restriction
curl -m 5 http://external-ip:8080  # Should timeout/fail
```

### Firewall Rules Applied
- Allow localhost access (127.0.0.1)
- Allow internal Docker network
- Block external access to services
- Allow SSH (port 22) for administration




## Screenshots & Evidence

Include screenshots of:
- ✅ Successful `docker-compose up` output
- ✅ Passing GitLab CI pipeline stages
- ✅ Prometheus targets and metrics
- ✅ Grafana dashboard with data
- ✅ Triggered alert in Alertmanager
- ✅ iptables rules verification
- ✅ Container restart after kill

## Additional Notes
- All services use restart policies for high availability
- Logs are centralized and rotated automatically
- Security scanning is integrated into CI pipeline
- Infrastructure as Code principles applied throughout

## Support
For issues or questions regarding this implementation, please check the logs first and refer to the troubleshooting section above.
