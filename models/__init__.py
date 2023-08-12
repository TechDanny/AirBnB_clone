#!/usr/bin/python3
"""
creates a unique FileStorage instance for the app
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
