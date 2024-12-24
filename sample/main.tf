# Don't forget to:
# az login

terraform {
  required_providers {
    azurerm = {
      source = "opentofu/azurerm"
      version = "4.3.0"
    }
  }
}

provider "azurerm" {
  subscription_id = var.subscription_id
  features {}
}

resource "azurerm_resource_group" "ai_resource_group" {
  name     = "ai-resources"
  location = "East US"
}

resource "azurerm_cognitive_account" "ai_cognitive_account" {
  name                = "ai-tts-service"
  location            = azurerm_resource_group.ai_resource_group.location
  resource_group_name = azurerm_resource_group.ai_resource_group.name
  kind                = "SpeechServices"
  sku_name            = "S0"
}

output "key" {
  value = azurerm_cognitive_account.ai_cognitive_account
  sensitive = true
}