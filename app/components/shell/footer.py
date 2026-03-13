import dash_mantine_components as dmc


def footer():
    return dmc.Box(
        dmc.Group(
            [
                dmc.Text("Poolantir", fw=700, size="sm"),
                dmc.Text(
                    "University of Iowa, Internet of Things 2026",
                    size="xs",
                    c="dimmed",
                ),
            ],
            justify="center",
            gap="xs",
            py="md",
        ),
        style={
            "border-top": "1px solid var(--app-shell-border-color)",
        },
    )
