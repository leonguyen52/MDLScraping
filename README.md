<div align="center">
  <h1>Original Work by kuryana</h1>
  <h1>Modified to match personal purposes</h1>

  <p>A simple MyDramaList.com scraper api.</p>
  <p>This scrapes on the go so it might be slow.</p>

  <h4>THIS SERVICE IS ONLY CREATED TO SATISFY THE NEED FOR AN API FOR [MYDRAMALIST.COM](https://mydramalist.com). THIS WILL BE STOPPED ONCE AN OFFICIAL API WILL BE RELEASED.</h4>

### Deploy Your Own

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/git/external?repository-url=https%3A%2F%2Fgithub.com%2FTheBoringDude%2Fkuryana)

</div>

## API Use

- [Search for dramas](https://my-domain.com/search/q/)

```
https://my-domain.com/search/q/{yourquery}
```

- [Get DRAMA Info](https://my-domain.com/id/)

```
https://my-domain.com/id/{mydramalist-slug}
```

- [Get DRAMA Cast](https://my-domain.com/id/{id}/cast)

```
https://my-domain.com/id/{mydramalist-slug}/cast
```

- [Get DRAMA Reviews](https://my-domain.com/id/{id}/reviews)

```
https://my-domain.com/id/{mydramalist-slug}/reviews
```

- [Get Person(People) Info](https://my-domain.com/people/)

```
https://my-domain.com/people/{people-id}
```

- [Get seasonal drama](https://my-domain.com/seasonal/)

```
https://my-domain.com/seasonal/{year}/{quarter}
```

## Development

- Using the vercel CLI (`localhost:3000`)
  ```
  vercel dev
  ```
- uvicorn (`localhost:8000`)
  ```
  uvicorn api.main --reload
  ```

## NOTE:

All Requests and SCRAPED Datas are not cached by Vercel or the API itself.

#### &copy; TheBoringDude
