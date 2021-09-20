import datetime
from typing import Optional

from database import db
from main.models.shortcut import ShortcutModel


def save_new_short_url(url: str, short_url: str) -> Optional[bool]:
    new_url = ShortcutModel(
            url=url,
            short_url=short_url,
            at_create=datetime.datetime.utcnow()
    )
    save_changes(new_url)
    return True



def check_for_free(short_url: str):
    return ShortcutModel.query.filter_by(short_url=short_url).first() is None


def get_url(short_url: str):
    shortcut = ShortcutModel.query.filter_by(short_url=short_url).first()
    if shortcut:
        return shortcut.url


def save_changes(data) -> None:
    db.session.add(data)
    db.session.commit()