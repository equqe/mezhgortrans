variable "yandex_token" {
  description = "Yandex Cloud OAuth token"
}

variable "yandex_cloud_id" {
  description = "Yandex Cloud ID"
}

variable "yandex_folder_id" {
  description = "Yandex Folder ID"
}

variable "yandex_zone" {
  description = "Yandex Zone"
  default     = "ru-central1-a"
}

variable "ssh_public_key_path" {
  description = "Path to the public SSH key"
}
