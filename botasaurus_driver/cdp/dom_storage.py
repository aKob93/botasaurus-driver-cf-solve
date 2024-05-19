# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: DOMStorage (experimental)

from __future__ import annotations

import typing
from dataclasses import dataclass

from .util import event_class, T_JSON_DICT


class SerializedStorageKey(str):
    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> SerializedStorageKey:
        return cls(json)

    def __repr__(self):
        return "SerializedStorageKey({})".format(super().__repr__())


@dataclass
class StorageId:
    """
    DOM Storage identifier.
    """

    #: Whether the storage is local storage (not session storage).
    is_local_storage: bool

    #: Security origin for the storage.
    security_origin: typing.Optional[str] = None

    #: Represents a key by which DOM Storage keys its CachedStorageAreas
    storage_key: typing.Optional[SerializedStorageKey] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["isLocalStorage"] = self.is_local_storage
        if self.security_origin is not None:
            json["securityOrigin"] = self.security_origin
        if self.storage_key is not None:
            json["storageKey"] = self.storage_key.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> StorageId:
        return cls(
            is_local_storage=bool(json["isLocalStorage"]),
            security_origin=(
                str(json["securityOrigin"])
                if json.get("securityOrigin", None) is not None
                else None
            ),
            storage_key=(
                SerializedStorageKey.from_json(json["storageKey"])
                if json.get("storageKey", None) is not None
                else None
            ),
        )


class Item(list):
    """
    DOM Storage item.
    """

    def to_json(self) -> typing.List[str]:
        return self

    @classmethod
    def from_json(cls, json: typing.List[str]) -> Item:
        return cls(json)

    def __repr__(self):
        return "Item({})".format(super().__repr__())


def clear(storage_id: StorageId) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    :param storage_id:
    """
    params: T_JSON_DICT = dict()
    params["storageId"] = storage_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "DOMStorage.clear",
        "params": params,
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables storage tracking, prevents storage events from being sent to the client.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "DOMStorage.disable",
    }
    json = yield cmd_dict


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables storage tracking, storage events will now be delivered to the client.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "DOMStorage.enable",
    }
    json = yield cmd_dict


def get_dom_storage_items(
    storage_id: StorageId,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[Item]]:
    """
    :param storage_id:
    :returns:
    """
    params: T_JSON_DICT = dict()
    params["storageId"] = storage_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "DOMStorage.getDOMStorageItems",
        "params": params,
    }
    json = yield cmd_dict
    return [Item.from_json(i) for i in json["entries"]]


def remove_dom_storage_item(
    storage_id: StorageId, key: str
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    :param storage_id:
    :param key:
    """
    params: T_JSON_DICT = dict()
    params["storageId"] = storage_id.to_json()
    params["key"] = key
    cmd_dict: T_JSON_DICT = {
        "method": "DOMStorage.removeDOMStorageItem",
        "params": params,
    }
    json = yield cmd_dict


def set_dom_storage_item(
    storage_id: StorageId, key: str, value: str
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    :param storage_id:
    :param key:
    :param value:
    """
    params: T_JSON_DICT = dict()
    params["storageId"] = storage_id.to_json()
    params["key"] = key
    params["value"] = value
    cmd_dict: T_JSON_DICT = {
        "method": "DOMStorage.setDOMStorageItem",
        "params": params,
    }
    json = yield cmd_dict


@event_class("DOMStorage.domStorageItemAdded")
@dataclass
class DomStorageItemAdded:
    storage_id: StorageId
    key: str
    new_value: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DomStorageItemAdded:
        return cls(
            storage_id=StorageId.from_json(json["storageId"]),
            key=str(json["key"]),
            new_value=str(json["newValue"]),
        )


@event_class("DOMStorage.domStorageItemRemoved")
@dataclass
class DomStorageItemRemoved:
    storage_id: StorageId
    key: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DomStorageItemRemoved:
        return cls(
            storage_id=StorageId.from_json(json["storageId"]), key=str(json["key"])
        )


@event_class("DOMStorage.domStorageItemUpdated")
@dataclass
class DomStorageItemUpdated:
    storage_id: StorageId
    key: str
    old_value: str
    new_value: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DomStorageItemUpdated:
        return cls(
            storage_id=StorageId.from_json(json["storageId"]),
            key=str(json["key"]),
            old_value=str(json["oldValue"]),
            new_value=str(json["newValue"]),
        )


@event_class("DOMStorage.domStorageItemsCleared")
@dataclass
class DomStorageItemsCleared:
    storage_id: StorageId

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DomStorageItemsCleared:
        return cls(storage_id=StorageId.from_json(json["storageId"]))
