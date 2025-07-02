# Azure Deployment Architecture

## High-Level Architecture Diagram

```mermaid
graph TB
    subgraph "GitHub Copilot Client"
        GC[GitHub Copilot]
    end
    
    subgraph "Azure Public Zone"
        AG[Azure Application Gateway<br/>SSL Termination]
        PIP[Public IP Address]
    end
    
    subgraph "Azure Virtual Network (10.0.0.0/16)"
        subgraph "App Subnet (10.0.1.0/24)"
            ACA[Azure Container Apps<br/>MCP Server]
        end
        
        subgraph "Private Endpoint Subnet (10.0.2.0/24)"
            PE1[Private Endpoint<br/>Azure OpenAI]
            PE2[Private Endpoint<br/>Key Vault]
            PE3[Private Endpoint<br/>Storage]
        end
        
        NSG[Network Security Groups]
    end
    
    subgraph "Azure Services"
        AOI[Azure OpenAI Service<br/>GPT-4 Turbo]
        KV[Azure Key Vault<br/>Secrets & Certs]
        SA[Storage Account<br/>Logs & Config]
        AM[Azure Monitor<br/>Logging & Metrics]
        DNS[Private DNS Zone]
    end
    
    subgraph "Azure Management"
        ARM[Azure Resource Manager]
        SUB[Azure Subscription]
    end
    
    %% Connections
    GC -->|HTTPS/SSL| PIP
    PIP --> AG
    AG -->|Internal Traffic| ACA
    ACA -->|Private Connection| PE1
    ACA -->|Private Connection| PE2
    ACA -->|Private Connection| PE3
    PE1 --> AOI
    PE2 --> KV
    PE3 --> SA
    ACA --> AM
    ACA -->|Azure SDK| ARM
    ARM --> SUB
    DNS -->|Name Resolution| PE1
    DNS -->|Name Resolution| PE2
    DNS -->|Name Resolution| PE3
    
    %% Styling
    classDef azure fill:#0078d4,stroke:#004578,stroke-width:2px,color:#fff
    classDef private fill:#00bcf2,stroke:#0078d4,stroke-width:2px,color:#fff
    classDef public fill:#ff6b35,stroke:#cc4125,stroke-width:2px,color:#fff
    
    class AG,PIP public
    class ACA,PE1,PE2,PE3,NSG private
    class AOI,KV,SA,AM,ARM,SUB,DNS azure
```

## Network Flow

1. **Client Connection**: GitHub Copilot connects via HTTPS to the public IP address
2. **SSL Termination**: Application Gateway terminates SSL and forwards to container apps
3. **Private Communication**: All internal Azure service communication uses private endpoints
4. **Azure SDK Integration**: MCP server uses Azure Management SDK to query resources
5. **AI Processing**: Requests are processed using Azure OpenAI via private endpoint

## Security Layers

- **External**: Public IP with Application Gateway WAF protection
- **Network**: VNet isolation with Network Security Groups
- **Transport**: SSL/TLS encryption for all external communication
- **Application**: Managed Identity for service-to-service authentication
- **Data**: Private endpoints for all Azure services, Key Vault for secrets

## Cost Optimization Features

- **Auto-scaling**: Container apps scale based on demand (1-5 instances)
- **Regional Deployment**: Single region deployment to minimize data transfer costs
- **Reserved Instances**: Application Gateway with reserved capacity
- **Monitoring**: Proactive monitoring to prevent cost overruns