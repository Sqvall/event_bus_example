from app.core.events_wire_up import events_wire_up


def app_factory(db) -> "FastAPI":
    return ...


async def app_startup(application):
    events_wire_up(application.db)


app = app_factory(...)


@app.on_event("startup")
async def startup():
    await app_startup(app)
