provider "yandex" {
  token     = var.yandex_token
  cloud_id  = var.yandex_cloud_id
  folder_id = var.yandex_folder_id
  zone      = var.yandex_zone
}

resource "yandex_vpc_network" "my_network" {
  name = "my-network"
}

resource "yandex_vpc_subnet" "my_subnet" {
  name          = "my-subnet"
  zone          = var.yandex_zone
  network_id    = yandex_vpc_network.my_network.id
  v4_cidr_block = "192.168.10.0/24"
}

resource "yandex_compute_instance" "my_instance" {
  name        = "my-instance"
  zone        = var.yandex_zone
  platform_id = "standard-v1"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd827b91d99psvq5fjit" # Ubuntu 20.04 LTS
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.my_subnet.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file(var.ssh_public_key_path)}"
  }
}

output "instance_ip" {
  value = yandex_compute_instance.my_instance.network_interface[0].nat_ip_address
}
