import { useEffect, useState } from 'react'
import useThrottle from './useThrottle'

export default function useSearchThrottle(
  defaultValue?: string,
  cb?: () => void,
) {
  const [search, setSearch] = useState(defaultValue || '')
  const [searchInput, setSearchInput] = useState(search)
  const searchItems = useThrottle((search: string) => {
    setSearch(search)
    cb?.()
  }, 100)
  useEffect(() => {
    searchItems(searchInput)
    //eslint-disable-next-line
    }, [searchInput]);
  return { search, searchInput, setSearchInput }
}
/* Usage example:
const searchItems =  useThrottle((search:string) => {
  doThing()
}, 100)
*/
