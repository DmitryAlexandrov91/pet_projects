from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .db_utils import Item, DATABASE_URL, Thing


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
                f"Предмет с партом {item['part_number']} уже есть в базе!")
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
                f"Ошибка: {e}. Пропущен парт {item['part_number']}.")
        except Exception as e:
            self.session.rollback()
            spider.logger.error(
                f"Ошибка: {e}. Ошибка записи в бд парта {item['part_number']}."
                )
        finally:
            return item

    def close_spider(self, spider):
        self.session.close()


class HaddanWearPipeline:

    def open_spider(self, spider):
        engine = create_engine(DATABASE_URL, echo=False)
        self.session = Session(engine)

    def process_item(self, item, spider):
        existing_thing = self.session.query(
            Thing).filter_by(
                serial_number=item['serial_number']
                ).first()
        if existing_thing:
            spider.logger.info(
                f"Предмет с S/N {item['serial_number']} уже есть в базе!")
            return item
        new_thing = Thing(
                part_number=item['part_number'],
                name=item['name'],
                type=item['type'],
                href=item['href'],
                owner=item['owner'],
                serial_number=item['serial_number']
            )
        try:
            self.session.add(new_thing)
            self.session.commit()
        except IntegrityError as e:
            self.session.rollback()
            spider.logger.error(
                f"Ошибка: {e}. Пропущен S/N {item['serial_number']}.")
        except Exception as e:
            self.session.rollback()
            spider.logger.error(
                f"Ошибка: {e}. Ошибка записи в бд S/N {item['serial_number']}."
                )
        finally:
            return item

    def close_spider(self, spider):
        self.session.close()
