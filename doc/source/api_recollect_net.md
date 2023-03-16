# City of Calgary

Support for schedules provided by [City of Calgary](https://www.calgary.ca/waste/residential/garbage-schedule.html).

## Configuration via configuration.yaml

```yaml
waste_collection_schedule:
  sources:
    - name: api_recollect_net
      args:
        address: ADDRESS
```

### Configuration Variables

**address**  
*(string) (required)*

## Example

```yaml
waste_collection_schedule:
  sources:
    - name: api_recollect_net
      args:
        street_address: address
```

## How to verify that your address works

Visit the [City of Calgary](https://www.calgary.ca/waste/residential/garbage-schedule.html) page and search for your address. The string you search for there should match the string in theaddress argument.
