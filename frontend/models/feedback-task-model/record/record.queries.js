import { Record as RecordModel } from "./Record.model";

// UPSERT
const upsertRecords = (records) => {
  RecordModel.insertOrUpdate({ data: records });
};

// GET
const getRecordWithFieldsByDatasetId = (
  datasetId,
  numberOfRecord = 1,
  fromRecord = 0
) => {
  return RecordModel.query()
    .with("record_fields")
    .where("dataset_id", datasetId)
    .limit(numberOfRecord)
    .offset(fromRecord)
    .first();
};
export { upsertRecords, getRecordWithFieldsByDatasetId };