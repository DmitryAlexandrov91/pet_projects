from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .db_utils import Item, DATABASE_URL


class HaddanItemsPipeline:

    def open_spider(self, spider):
        engine = create_engine(DATABASE_URL, echo=False)
        self.session = Session(engine)

    def process_item(self, item, spider):
        existing_thing = self.session.query(
            Item).filter_by(
                part_number=item['part_number']
                ).first()
        if existing_thing:
            spider.logger.info(
                f"Item with part_number={item['part_number']} already exists. Skipping.")
            return item
        new_item = Item(
                part_number=item['part_number'],
                name=item['name'],
                type=item['type'],
                href=item['href'],
            )
        try:
            self.session.add(new_item)
            self.session.commit()
        except IntegrityError as e:
            self.session.rollback()
            spider.logger.error(
                f"IntegrityError: {e}. Skipping item with part_number={item['part_number']}.")
        except Exception as e:
            self.session.rollback()
            spider.logger.error(
                f"Error: {e}. Failed to add item with part_number={item['part_number']}.")
        finally:
            return item

    def close_spider(self, spider):
        self.session.close()
