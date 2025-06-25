
data "external_schema" "sqlalchemy" {
  program = [
    "atlas-provider-sqlalchemy",
    "--path", "./tables",
    "--dialect", "postgresql"
  ]
}

env "sqlalchemy" {
  src = data.external_schema.sqlalchemy.url
  dev = "docker://postgres/16/dev?search_path=public"
  lint {
    non_linear {
      error = true
    }
    destructive {
      error = true
    }
    data_depend {
      error = true
    }
  }
  migration {
    dir = "file://migrations"
  }
  format {
    migrate {
      diff = "{{ sql . \"  \" }}"
    }
  }
}
