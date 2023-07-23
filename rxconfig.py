import reflex as rx

class MyportfolioConfig(rx.Config):
    pass

config = MyportfolioConfig(
    app_name="myPortFolio",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)