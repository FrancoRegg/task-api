from app.db.session import engine
from app.models import Base   # Base conoce todos los modelos


def main() -> None:
    print("Creando tablas...")
    Base.metadata.create_all(bind=engine)
    print("Listo.")


if __name__ == "__main__":
    main()
